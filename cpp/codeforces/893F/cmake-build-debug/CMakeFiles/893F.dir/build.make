# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2017.2.3\bin\cmake\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2017.2.3\bin\cmake\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/893F.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/893F.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/893F.dir/flags.make

CMakeFiles/893F.dir/main.cpp.obj: CMakeFiles/893F.dir/flags.make
CMakeFiles/893F.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/893F.dir/main.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\893F.dir\main.cpp.obj -c C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F\main.cpp

CMakeFiles/893F.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/893F.dir/main.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F\main.cpp > CMakeFiles\893F.dir\main.cpp.i

CMakeFiles/893F.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/893F.dir/main.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F\main.cpp -o CMakeFiles\893F.dir\main.cpp.s

CMakeFiles/893F.dir/main.cpp.obj.requires:

.PHONY : CMakeFiles/893F.dir/main.cpp.obj.requires

CMakeFiles/893F.dir/main.cpp.obj.provides: CMakeFiles/893F.dir/main.cpp.obj.requires
	$(MAKE) -f CMakeFiles\893F.dir\build.make CMakeFiles/893F.dir/main.cpp.obj.provides.build
.PHONY : CMakeFiles/893F.dir/main.cpp.obj.provides

CMakeFiles/893F.dir/main.cpp.obj.provides.build: CMakeFiles/893F.dir/main.cpp.obj


# Object files for target 893F
893F_OBJECTS = \
"CMakeFiles/893F.dir/main.cpp.obj"

# External object files for target 893F
893F_EXTERNAL_OBJECTS =

893F.exe: CMakeFiles/893F.dir/main.cpp.obj
893F.exe: CMakeFiles/893F.dir/build.make
893F.exe: CMakeFiles/893F.dir/linklibs.rsp
893F.exe: CMakeFiles/893F.dir/objects1.rsp
893F.exe: CMakeFiles/893F.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable 893F.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\893F.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/893F.dir/build: 893F.exe

.PHONY : CMakeFiles/893F.dir/build

CMakeFiles/893F.dir/requires: CMakeFiles/893F.dir/main.cpp.obj.requires

.PHONY : CMakeFiles/893F.dir/requires

CMakeFiles/893F.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\893F.dir\cmake_clean.cmake
.PHONY : CMakeFiles/893F.dir/clean

CMakeFiles/893F.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F\cmake-build-debug C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F\cmake-build-debug C:\Users\shhuan\Documents\git\algorithms\cpp\codeforces\893F\cmake-build-debug\CMakeFiles\893F.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/893F.dir/depend

