# Verification problems

## noH

Single element test for verifiying the correct implemetation of a trapezoidal
TSL.

Abaqus input files:

* `noH.inp`: job file
* `_AISI.inp`: include file with AISI steel material block
* `_coh.inp`: include file with coehesive TSL law (generated)
* `_mesh.inp`: include file with mesh definition
* `./results`: directory with reference results

Abaqus run instructions.

1) Generate the `_coh.inp` material block using the `gencoh.py` program
```bash
$ python ../../utils/gencoh.py 0.22e-3 9.7e-3 15e-3 1000 > _coh.inp
```
   The  generated file should be identical to `./results/_coh.inp`
2) Run abaqus
```bash
$ abaqus j=noH
```
3) Post-process results
```bash
$ abaqus odbreport odb=noH -mode html > noH-report.html
$ abaqus python post.py noH
```

Post-processing will generate the data file `noH.npz`, which is stored
in numpy [`.npz` format](http://docs.scipy.org/doc/numpy/reference/generated/numpy.savez.html). A reference results file is given in the `results` directory.
