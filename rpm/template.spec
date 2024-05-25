%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-octomap-server
Version:        2.2.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS octomap_server package

License:        BSD
URL:            http://www.ros.org/wiki/octomap_server
Source0:        %{name}-%{version}.tar.gz

Requires:       pcl-devel
Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-message-filters
Requires:       ros-jazzy-nav-msgs
Requires:       ros-jazzy-octomap
Requires:       ros-jazzy-octomap-msgs
Requires:       ros-jazzy-octomap-ros
Requires:       ros-jazzy-pcl-conversions
Requires:       ros-jazzy-pcl-ros
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-components
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-std-srvs
Requires:       ros-jazzy-tf2
Requires:       ros-jazzy-tf2-eigen
Requires:       ros-jazzy-tf2-geometry-msgs
Requires:       ros-jazzy-tf2-ros
Requires:       ros-jazzy-visualization-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  pcl-devel
BuildRequires:  ros-jazzy-ament-cmake-auto
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-message-filters
BuildRequires:  ros-jazzy-nav-msgs
BuildRequires:  ros-jazzy-octomap
BuildRequires:  ros-jazzy-octomap-msgs
BuildRequires:  ros-jazzy-octomap-ros
BuildRequires:  ros-jazzy-pcl-conversions
BuildRequires:  ros-jazzy-pcl-ros
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-components
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-std-srvs
BuildRequires:  ros-jazzy-tf2
BuildRequires:  ros-jazzy-tf2-eigen
BuildRequires:  ros-jazzy-tf2-geometry-msgs
BuildRequires:  ros-jazzy-tf2-ros
BuildRequires:  ros-jazzy-visualization-msgs
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-lint-auto
BuildRequires:  ros-jazzy-ament-lint-common
%endif

%description
octomap_server loads a 3D map (as Octree-based OctoMap) and distributes it to
other nodes in a compact binary format. It also allows to incrementally build 3D
OctoMaps, and provides map saving in the node octomap_saver.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Sat May 25 2024 Wolfgang Merkt <opensource@wolfgangmerkt.com> - 2.2.0-1
- Autogenerated by Bloom

* Fri Apr 19 2024 Wolfgang Merkt <opensource@wolfgangmerkt.com> - 2.1.0-3
- Autogenerated by Bloom

* Wed Mar 06 2024 Wolfgang Merkt <opensource@wolfgangmerkt.com> - 2.1.0-2
- Autogenerated by Bloom

