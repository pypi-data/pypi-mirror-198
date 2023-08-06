# del-msh

This is a utility library for static mesh written completely in Rust. 

Originally, the code is written in C++ in [DelFEM2](https://github.com/nobuyuki83/delfem2), then it was ported to Rust. 

See [the documentation generated from code](https://docs.rs/del-msh)

- [x] generating primitive meshes (sphere, cylinder, torus)
- [x] load/save wavefront obj mesh
- [x] unify indexes of texture vertex and position vertex
- [x] one-ring neighborhood 
- [x] adjacent element 