#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : cmake
Version  : 3.22.1
Release  : 303
URL      : file:///aot/build/clearlinux/packages/cmake/cmake-v3.22.1.tar.gz
Source0  : file:///aot/build/clearlinux/packages/cmake/cmake-v3.22.1.tar.gz
Summary  : General purpose data compression library
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0+
BuildRequires : SDL-dev
BuildRequires : SDL2-dev
BuildRequires : VTK-dev
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Headers-dev Vulkan-Loader-dev Vulkan-Tools
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Tools
BuildRequires : acl-dev
BuildRequires : acl-staticdev
BuildRequires : alsa-lib-dev
BuildRequires : armadillo-data
BuildRequires : bash
BuildRequires : bash coreutils gzip
BuildRequires : binutils-dev
BuildRequires : bison-dev
BuildRequires : boost-dev
BuildRequires : brotli
BuildRequires : brotli-dev
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : cairo-dev
BuildRequires : cairo-lib
BuildRequires : cmake
BuildRequires : coreutils
BuildRequires : cups-dev
BuildRequires : curl
BuildRequires : curl-dev
BuildRequires : curl-lib
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : doxygen
BuildRequires : e2fsprogs-dev
BuildRequires : elfutils-dev
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : extra-cmake-modules-data
BuildRequires : findutils
BuildRequires : flex
BuildRequires : fontconfig
BuildRequires : fontconfig-data
BuildRequires : fontconfig-dev
BuildRequires : fontconfig-lib
BuildRequires : fonts-clear
BuildRequires : freeglut-dev
BuildRequires : freetype
BuildRequires : freetype-dev
BuildRequires : freetype-lib
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdal-dev
BuildRequires : git
BuildRequires : glew-dev
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : gnutls-dev
BuildRequires : googletest-dev
BuildRequires : graphite
BuildRequires : graphite-dev
BuildRequires : gsl-dev
BuildRequires : gtk+-dev
BuildRequires : gzip
BuildRequires : harfbuzz-dev
BuildRequires : harfbuzz-lib
BuildRequires : hdf5-dev
BuildRequires : icu4c-dev
BuildRequires : icu4c-lib
BuildRequires : jsoncpp
BuildRequires : jsoncpp-dev
BuildRequires : jsoncpp-lib
BuildRequires : jsoncpp-staticdev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfixes-dev
BuildRequires : libXfont2-dev
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-lib
BuildRequires : libarchive
BuildRequires : libarchive-dev
BuildRequires : libarchive-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt-dev
BuildRequires : libgit2
BuildRequires : libgit2-dev
BuildRequires : libidn2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libogg-dev
BuildRequires : libpng-dev
BuildRequires : libsndfile-dev
BuildRequires : libssh-dev
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libunistring
BuildRequires : libunistring-dev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : libvorbis-dev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt-dev
BuildRequires : lua-dev
BuildRequires : lz4
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : m4
BuildRequires : md4c
BuildRequires : md4c-dev
BuildRequires : mesa-dev
BuildRequires : ncurses-dev
BuildRequires : nghttp2
BuildRequires : nghttp2-dev
BuildRequires : openblas
BuildRequires : opencl-headers-dev
BuildRequires : openjdk13
BuildRequires : openjdk13-dev
BuildRequires : openmpi-dev
BuildRequires : openssh
BuildRequires : openssl-dev
BuildRequires : openssl-lib
BuildRequires : openssl-staticdev
BuildRequires : opus-dev
BuildRequires : p11-kit
BuildRequires : p11-kit-dev
BuildRequires : patch
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pcre2-dev
BuildRequires : pcre2-staticdev
BuildRequires : perl
BuildRequires : php-dev
BuildRequires : pixman-dev
BuildRequires : pixman-lib
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(glut)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libexslt)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libxslt)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(xrender)
BuildRequires : postgresql-dev
BuildRequires : protobuf-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : qtbase
BuildRequires : qtbase-dev
BuildRequires : qtdeclarative
BuildRequires : qtdeclarative-dev
BuildRequires : qtlocation
BuildRequires : qtlocation-dev
BuildRequires : qtsvg
BuildRequires : qtsvg-dev
BuildRequires : qttools
BuildRequires : qttools-dev
BuildRequires : qtwebchannel
BuildRequires : qtwebchannel-dev
BuildRequires : qtwebengine
BuildRequires : qtwebengine-dev
BuildRequires : qtx11extras-dev
BuildRequires : requests
BuildRequires : ruby
BuildRequires : setxkbmap
BuildRequires : sqlite-autoconf
BuildRequires : sqlite-autoconf-dev
BuildRequires : subversion
BuildRequires : swig
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-dev tk-dev
BuildRequires : texlive
BuildRequires : tiff-dev
BuildRequires : tk-dev
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : wayland
BuildRequires : wayland-dev
BuildRequires : wget
BuildRequires : xauth
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: fix-x11.patch

%description
ZLIB DATA COMPRESSION LIBRARY
zlib 1.2.3 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://www.ietf.org/rfc/rfc1950.txt (zlib format), rfc1951.txt (deflate format)
and rfc1952.txt (gzip format). These documents are also available in other
formats from ftp://ftp.uu.net/graphics/png/documents/zlib/zdoc-index.html

%prep
%setup -q -n cmake
cd %{_builddir}/cmake
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640257205
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
unset ASFLAGS
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage -fprofile-partial-training -fprofile-correction -freorder-functions --coverage -lgcov"
export CFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export ASMFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LIBS_GENERATE="-lgcov"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize -fopt-info-vec
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-Wmissing-profile -Wcoverage-mismatch -fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-partial-training -fprofile-correction -freorder-functions"
export CFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export ASMFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=1
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
export ASMFLAGS="${ASMFLAGS_GENERATE}"
export LIBS="${LIBS_GENERATE}"
%cmake ..   -DCMAKE_USE_SYSTEM_EXPAT:BOOL=ON \
-DCMAKE_USE_SYSTEM_ZSTD:BOOL=ON \
-DCMAKE_USE_SYSTEM_CURL:BOOL=ON \
-DCMAKE_USE_SYSTEM_ZLIB:BOOL=ON \
-DCMAKE_USE_SYSTEM_LIBLZMA:BOOL=ON \
-DCMAKE_USE_SYSTEM_BZIP2:BOOL=ON \
-DCMAKE_USE_SYSTEM_LIBARCHIVE:BOOL=ON \
-DCMAKE_USE_SYSTEM_JSONCPP:BOOL=ON \
-DCMAKE_USE_SYSTEM_LIBRARY_NGHTTP2:BOOL=ON \
-DCMake_BUILD_LTO:BOOL=OFF \
-DCMAKE_BUILD_LTO:BOOL=OFF \
-DBUILD_QtDialog:BOOL=ON \
-DBUILD_CursesDialog:BOOL=ON \
-DBUILD_SHARED_LIBS:BOOL=OFF \
-DBUILD_STATIC_LIBS:BOOL=ON \
-DBUILD_TESTING:BOOL=ON
## make_prepend content
sd "/usr/lib64/libz.so" "/usr/lib64/libz.a" $(fd -uu link.txt)
sd "/usr/lib64/libexpat.so" "/usr/lib64/libexpat.a" $(fd -uu link.txt)
sd "/usr/lib64/libjsoncpp.so" "/usr/lib64/libjsoncpp.a" $(fd -uu link.txt)
sd "/usr/lib64/libarchive.a" "/usr/lib64/libarchive.a /usr/lib64/libssl.a /usr/lib64/libcrypto.a /usr/lib64/libacl.a /usr/lib64/liblzo2.a /usr/lib64/liblzma.a /usr/lib64/libzstd.a /usr/lib64/liblz4.a /usr/lib64/libbz2.a /usr/lib64/libz.a /usr/lib64/libxml2.a /usr/lib64/liblzma.a /usr/lib64/libz.a" $(fd -uu link.txt)
#sd "/usr/lib64/libcurl.so" "/usr/lib64/libcurl.a -lnghttp2 /usr/lib64/libidn2.a /usr/lib64/libunistring.a /usr/lib64/libssl.a /usr/lib64/libcrypto.a /usr/lib64/libzstd.a /usr/lib64/libbrotlidec.a /usr/lib64/libz.a" $(fd -uu link.txt)
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1

## profile_payload start
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
ctest --parallel 1 -V --progress || :
exit 1
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
## profile_payload end
find . -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
export ASMFLAGS="${ASMFLAGS_USE}"
export LIBS="${LIBS_USE}"
%cmake .. -DCMAKE_USE_SYSTEM_EXPAT:BOOL=ON \
-DCMAKE_USE_SYSTEM_ZSTD:BOOL=ON \
-DCMAKE_USE_SYSTEM_CURL:BOOL=ON \
-DCMAKE_USE_SYSTEM_ZLIB:BOOL=ON \
-DCMAKE_USE_SYSTEM_LIBLZMA:BOOL=ON \
-DCMAKE_USE_SYSTEM_BZIP2:BOOL=ON \
-DCMAKE_USE_SYSTEM_LIBARCHIVE:BOOL=ON \
-DCMAKE_USE_SYSTEM_JSONCPP:BOOL=ON \
-DCMAKE_USE_SYSTEM_LIBRARY_NGHTTP2:BOOL=ON \
-DCMake_BUILD_LTO:BOOL=OFF \
-DCMAKE_BUILD_LTO:BOOL=OFF \
-DBUILD_QtDialog:BOOL=ON \
-DBUILD_CursesDialog:BOOL=ON \
-DBUILD_SHARED_LIBS:BOOL=OFF \
-DBUILD_STATIC_LIBS:BOOL=ON \
-DBUILD_TESTING:BOOL=OFF
## make_prepend content
sd "/usr/lib64/libz.so" "/usr/lib64/libz.a" $(fd -uu link.txt)
sd "/usr/lib64/libexpat.so" "/usr/lib64/libexpat.a" $(fd -uu link.txt)
sd "/usr/lib64/libjsoncpp.so" "/usr/lib64/libjsoncpp.a" $(fd -uu link.txt)
sd "/usr/lib64/libarchive.a" "/usr/lib64/libarchive.a /usr/lib64/libssl.a /usr/lib64/libcrypto.a /usr/lib64/libacl.a /usr/lib64/liblzo2.a /usr/lib64/liblzma.a /usr/lib64/libzstd.a /usr/lib64/liblz4.a /usr/lib64/libbz2.a /usr/lib64/libz.a /usr/lib64/libxml2.a /usr/lib64/liblzma.a /usr/lib64/libz.a" $(fd -uu link.txt)
#sd "/usr/lib64/libcurl.so" "/usr/lib64/libcurl.a -lnghttp2 /usr/lib64/libidn2.a /usr/lib64/libunistring.a /usr/lib64/libssl.a /usr/lib64/libcrypto.a /usr/lib64/libzstd.a /usr/lib64/libbrotlidec.a /usr/lib64/libz.a" $(fd -uu link.txt)
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
fi
popd

%install
export SOURCE_DATE_EPOCH=1640257205
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
