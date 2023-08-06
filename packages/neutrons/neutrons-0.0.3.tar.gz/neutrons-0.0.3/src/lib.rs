pub mod colours;
pub mod data;
pub mod engine;
pub mod model;
pub mod parameters;
pub mod particle;
pub mod run;

pub use self::colours::*;
pub use self::data::*;
pub use self::engine::*;
pub use self::model::*;
pub use self::parameters::*;
pub use self::particle::*;
pub use self::run::*;

use pyo3::prelude::*;
use rand::rngs::ThreadRng;
use std::{env::current_dir, f64::consts::PI, fs::create_dir, path::PathBuf};

/// Runs a simulation.
#[pyfunction]
fn simulate(
    num_threads: usize,
    num_steps: usize,
    colour_map: Vec<String>,
    num_neutrons: usize,
    block_size: usize,
    bump_dist: f64,
    min_weight: f64,
    gun_pos: [f64; 3],
    gun_target: [f64; 3],
    gun_spread: f64,
    scat_coeff: f64,
    abs_coeff: f64,
    mins: [f64; 3],
    maxs: [f64; 3],
    num_voxels: [usize; 3],
) -> PyResult<String> {
    let params = parameters::Parameters {
        num_threads,
        num_steps,
        colour_map,
        num_neutrons,
        block_size,
        bump_dist,
        min_weight,
        gun_pos,
        gun_target,
        gun_spread: gun_spread * PI / 180.0,
        scat_coeff,
        abs_coeff,
        mins,
        maxs,
        num_voxels,
    };

    entrypoint(&params);

    Ok("Simulation complete.".to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn neutrons(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(simulate, m)?)?;
    Ok(())
}

/// Simulation entrypoint.
fn entrypoint(params: &parameters::Parameters) {
    // Setup directories.
    let cwd = current_dir().expect("Failed to determine current working directory");
    let (in_dir, out_dir) = (cwd.join("input"), cwd.join("output"));
    init_dirs(&in_dir, &out_dir);

    // Build model.
    let model = Model::new(&params);

    // Run the simulation.
    let mut data = Data::new(model.grid.num_voxels);
    let num_steps = params.num_steps.min(params.num_neutrons);

    for step in 0..num_steps {
        data = run::multi_thread(
            data,
            params.num_neutrons / num_steps,
            params.block_size,
            &model,
            my_engine,
        );
        data.save(&model.colour_map, &out_dir, step);
    }
}

/// Initialise the input and output directories.
fn init_dirs(_input: &PathBuf, output: &PathBuf) {
    // if !input.exists() {
    //     create_dir(&input).expect("Failed to create input directory");
    // }

    if !output.exists() {
        create_dir(&output).expect("Failed to create output directory");
    }

    let subdirs = vec![
        "scatters_x",
        "scatters_y",
        "scatters_z",
        "distance_x",
        "distance_y",
        "distance_z",
    ];
    for subdir in subdirs {
        let dir_path = output.join(subdir);
        if !dir_path.exists() {
            create_dir(&dir_path).expect(&format!("Failed to create {} output directory", subdir));
        }
    }
}

/// Inject a neutron into the model
fn my_engine(_i: usize, rng: &mut ThreadRng, model: &Model, data: &mut Data) {
    // Generate a random neutron.
    let mut neutron = model.generate_neutron(rng);

    // Inject the neutron into the model.
    let dist_side = model.grid.boundary.dist_side(&neutron.ray);
    if let Some((dist, side)) = dist_side {
        if !side.is_inside() {
            neutron.travel(dist + model.bump_dist);
        }
    } else {
        panic!("Failed to inject neutron into the grid.")
    }

    // Sample the model.
    sample(neutron, rng, model, data);

    // Sample complete.
    data.total += 1;
}

/// Sample the model.
fn sample(mut neutron: Particle, rng: &mut ThreadRng, model: &Model, data: &mut Data) {
    while let Some(index) = model.grid.voxel_index(&neutron.ray.pos) {
        let voxel = model.grid.generate_voxel(index);
        let mut dist_travelled = 0.0;
        loop {
            if let Some(voxel_dist) = voxel.dist(&neutron.ray) {
                let r = rand::random::<f64>();
                let scatter_dist = -(r.ln()) / model.interaction_coeff;

                if scatter_dist < voxel_dist {
                    // Scattering event.
                    neutron.travel(scatter_dist);
                    dist_travelled += scatter_dist;
                    neutron.scatter(rng);
                    neutron.weight *= model.albedo;
                    data.scatters[index] += neutron.weight;

                    if neutron.weight < model.min_weight {
                        // Neutron has been absorbed.
                        data.absorbed += 1;
                        return;
                    }
                } else {
                    neutron.travel(voxel_dist + model.bump_dist);
                    dist_travelled += voxel_dist + model.bump_dist;
                    break;
                }
            } else {
                println!(
                    "[WARN!] Neutron escaped the grid at: {}\t{}\t{}",
                    neutron.ray.pos.x, neutron.ray.pos.y, neutron.ray.pos.z
                );
            }
        }
        data.travelled[index] += dist_travelled;
    }

    // Neutron escaped the grid.
    data.escaped += 1;
}
