# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

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

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build

# Include any dependencies generated for this target.
include tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/depend.make

# Include the progress variables for this target.
include tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/progress.make

# Include the compile flags for this target's objects.
include tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/flags.make

tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/main.c.o: tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/flags.make
tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/main.c.o: ../tools/sensor_cmds/main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/main.c.o"
	cd /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build/tools/sensor_cmds && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sensor_cmds.dir/main.c.o   -c /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/tools/sensor_cmds/main.c

tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sensor_cmds.dir/main.c.i"
	cd /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build/tools/sensor_cmds && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/tools/sensor_cmds/main.c > CMakeFiles/sensor_cmds.dir/main.c.i

tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sensor_cmds.dir/main.c.s"
	cd /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build/tools/sensor_cmds && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/tools/sensor_cmds/main.c -o CMakeFiles/sensor_cmds.dir/main.c.s

# Object files for target sensor_cmds
sensor_cmds_OBJECTS = \
"CMakeFiles/sensor_cmds.dir/main.c.o"

# External object files for target sensor_cmds
sensor_cmds_EXTERNAL_OBJECTS =

tools/sensor_cmds/sensor_cmds: tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/main.c.o
tools/sensor_cmds/sensor_cmds: tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/build.make
tools/sensor_cmds/sensor_cmds: libsensor_commands.so.0.0.1
tools/sensor_cmds/sensor_cmds: tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable sensor_cmds"
	cd /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build/tools/sensor_cmds && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sensor_cmds.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/build: tools/sensor_cmds/sensor_cmds

.PHONY : tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/build

tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/clean:
	cd /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build/tools/sensor_cmds && $(CMAKE_COMMAND) -P CMakeFiles/sensor_cmds.dir/cmake_clean.cmake
.PHONY : tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/clean

tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/depend:
	cd /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/tools/sensor_cmds /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build/tools/sensor_cmds /home/arkantos/Desktop/Diseno_Software/ie0417-dev/labs/lab3/sensor_commands/build/tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tools/sensor_cmds/CMakeFiles/sensor_cmds.dir/depend

