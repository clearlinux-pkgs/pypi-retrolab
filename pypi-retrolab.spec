#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v20
# autospec commit: e180208
#
Name     : pypi-retrolab
Version  : 0.3.21
Release  : 11
URL      : https://files.pythonhosted.org/packages/e8/20/9d05642226797a72f7a04937f6c0e96a3fe3bce8400fbe8611b6ed26ffbc/retrolab-0.3.21.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/20/9d05642226797a72f7a04937f6c0e96a3fe3bce8400fbe8611b6ed26ffbc/retrolab-0.3.21.tar.gz
Summary  : JupyterLab Distribution with a retro look and feel
Group    : Development/Tools
License  : BSD-3-Clause HPND MIT
Requires: pypi-retrolab-bin = %{version}-%{release}
Requires: pypi-retrolab-data = %{version}-%{release}
Requires: pypi-retrolab-license = %{version}-%{release}
Requires: pypi-retrolab-python = %{version}-%{release}
Requires: pypi-retrolab-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jupyter_packaging)
BuildRequires : pypi(jupyterlab)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<h1 align="center">
<img
alt="RetroLab"
src="./logo.png"
width="256"
/>
</h1>
![Github Actions Status](https://github.com/jupyterlab/retrolab/workflows/Build/badge.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gist/jtpio/4a6a34da66b32249e28df718ec30e4d7/master?urlpath=/retro/notebooks/tour.ipynb)
[![Binder main](https://img.shields.io/badge/launch-main-E66581.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/jupyterlab/retrolab/main?urlpath=retro/tree)
[![PyPI](https://img.shields.io/pypi/v/retrolab.svg)](https://pypi.org/project/retrolab)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/retrolab.svg)](https://anaconda.org/conda-forge/retrolab)

%package bin
Summary: bin components for the pypi-retrolab package.
Group: Binaries
Requires: pypi-retrolab-data = %{version}-%{release}
Requires: pypi-retrolab-license = %{version}-%{release}

%description bin
bin components for the pypi-retrolab package.


%package data
Summary: data components for the pypi-retrolab package.
Group: Data

%description data
data components for the pypi-retrolab package.


%package license
Summary: license components for the pypi-retrolab package.
Group: Default

%description license
license components for the pypi-retrolab package.


%package python
Summary: python components for the pypi-retrolab package.
Group: Default
Requires: pypi-retrolab-python3 = %{version}-%{release}

%description python
python components for the pypi-retrolab package.


%package python3
Summary: python3 components for the pypi-retrolab package.
Group: Default
Requires: python3-core
Provides: pypi(retrolab)
Requires: pypi(jupyter_server)
Requires: pypi(jupyterlab)
Requires: pypi(jupyterlab_server)
Requires: pypi(nbclassic)
Requires: pypi(tornado)

%description python3
python3 components for the pypi-retrolab package.


%prep
%setup -q -n retrolab-0.3.21
cd %{_builddir}/retrolab-0.3.21
pushd ..
cp -a retrolab-0.3.21 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730157064
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . jupyterlab
pypi-dep-fix.py . nbclassic
pypi-dep-fix.py . jupyter-server
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . jupyterlab
pypi-dep-fix.py . nbclassic
pypi-dep-fix.py . jupyter-server
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-retrolab
cp %{_builddir}/retrolab-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-retrolab/76ae6497e3d51cbf847430871ee1961b57268a8d || :
cp %{_builddir}/retrolab-%{version}/retrolab/static/1542.bundle.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-retrolab/10645e5e81c59dc0f14b79252005ea68d42f1ba7 || :
cp %{_builddir}/retrolab-%{version}/retrolab/static/250.bundle.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-retrolab/cd522246a57b87ba54b1b6b92174b9091f70e983 || :
cp %{_builddir}/retrolab-%{version}/retrolab/static/4170.bundle.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-retrolab/01ebbe688c25d738b9ee0e2de8113f7351c88e7a || :
cp %{_builddir}/retrolab-%{version}/retrolab/static/6731.bundle.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-retrolab/cd522246a57b87ba54b1b6b92174b9091f70e983 || :
cp %{_builddir}/retrolab-%{version}/retrolab/static/6974.bundle.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-retrolab/12b795d0685923cc5e3b66695ca83149e427713e || :
cp %{_builddir}/retrolab-%{version}/retrolab/static/7378.bundle.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-retrolab/0036998e52f1b6442c90b9ea6df602bef0294cc5 || :
cp %{_builddir}/retrolab-%{version}/retrolab/static/7821.bundle.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-retrolab/cd522246a57b87ba54b1b6b92174b9091f70e983 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} jupyterlab
pypi-dep-fix.py %{buildroot} nbclassic
pypi-dep-fix.py %{buildroot} jupyter-server
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_notebook_config.d/retrolab.json
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_server_config.d/retrolab.json
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-retro

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/lab/schemas/@retrolab/application-extension/menus.json
/usr/share/jupyter/lab/schemas/@retrolab/application-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@retrolab/application-extension/top.json
/usr/share/jupyter/lab/schemas/@retrolab/notebook-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@retrolab/notebook-extension/scroll-output.json
/usr/share/jupyter/labextensions/@retrolab/lab-extension/package.json
/usr/share/jupyter/labextensions/@retrolab/lab-extension/schemas/@retrolab/lab-extension/interface-switcher.json
/usr/share/jupyter/labextensions/@retrolab/lab-extension/schemas/@retrolab/lab-extension/package.json.orig
/usr/share/jupyter/labextensions/@retrolab/lab-extension/static/568.43e96248ddabebd7d8c1.js
/usr/share/jupyter/labextensions/@retrolab/lab-extension/static/676.4ced5e44813c465d9d0d.js
/usr/share/jupyter/labextensions/@retrolab/lab-extension/static/697.212c1d6546c1a066a01f.js
/usr/share/jupyter/labextensions/@retrolab/lab-extension/static/776.d2dd2c76842bf87de493.js
/usr/share/jupyter/labextensions/@retrolab/lab-extension/static/974.a57245c4538e552cf996.js
/usr/share/jupyter/labextensions/@retrolab/lab-extension/static/remoteEntry.c8410055f1a8098c2874.js
/usr/share/jupyter/labextensions/@retrolab/lab-extension/static/style.js
/usr/share/jupyter/labextensions/@retrolab/lab-extension/static/third-party-licenses.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-retrolab/0036998e52f1b6442c90b9ea6df602bef0294cc5
/usr/share/package-licenses/pypi-retrolab/01ebbe688c25d738b9ee0e2de8113f7351c88e7a
/usr/share/package-licenses/pypi-retrolab/10645e5e81c59dc0f14b79252005ea68d42f1ba7
/usr/share/package-licenses/pypi-retrolab/12b795d0685923cc5e3b66695ca83149e427713e
/usr/share/package-licenses/pypi-retrolab/76ae6497e3d51cbf847430871ee1961b57268a8d
/usr/share/package-licenses/pypi-retrolab/cd522246a57b87ba54b1b6b92174b9091f70e983

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
