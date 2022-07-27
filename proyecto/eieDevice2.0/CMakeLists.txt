cmake_minimum_required(VERSION 3.16)

project(eieDevice VERSION 1.0)

# Set default build type to release
if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()
message(STATUS "Current build type: ${CMAKE_BUILD_TYPE}")

# Include rules
include(FindPkgConfig)
include(utils.cmake)
include(CTest)


# Dependencies
pkg_check_modules(CJSON REQUIRED libcjson>=1.7.15)
add_definitions(${CJSON_CFLAGS})
link_directories(${CJSON_LIBRARY_DIRS})
include_directories(${CJSON_INCLUDE_DIRS})

set(INCLUDE_DIR ${CMAKE_SOURCE_DIR}/include)
set(CONFIG_DIR ${CMAKE_SOURCE_DIR}/config)

include_directories(${INCLUDE_DIR})

install(
  DIRECTORY ${INCLUDE_DIR}/${LIB_NAME}
  DESTINATION include
  FILES_MATCHING PATTERN "*.h"
  PATTERN "_*" EXCLUDE
  PATTERN "external" EXCLUDE
)

# Build flags
set(C_WARNINGS "-Wall -Wstrict-prototypes -Wshadow")
set(CXX_WARNINGS "-Wall -Wshadow")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu11 ${C_WARNINGS}")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11 ${CXX_WARNINGS}")


# Shared library
ADD_LIB_DIRS(src)

set(VERSION_SOURCE ${CMAKE_BINARY_DIR}/src/version.c)
configure_file(
  src/version.c.in
  "${VERSION_SOURCE}"
  @ONLY
)
list(APPEND LIB_SOURCES ${VERSION_SOURCE})

add_library(${LIB_NAME} SHARED ${LIB_SOURCES})

install(
  TARGETS ${LIB_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
)


# Testing
add_subdirectory(test EXCLUDE_FROM_ALL)

add_subdirectory(tools)



