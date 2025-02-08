# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -std=c++17

LDFLAGS =  $(shell pkg-config --libs sdl2 SDL2_ttf) -I/usr/include/eigen3/Eigen 
# Target executable
BUILD_DIR = build
TARGET = ${BUILD_DIR}/project

# Source files
SRCS := $(wildcard src/*.cc)

# Object files (derived from source files, placed in the build directory)
OBJS = $(patsubst src/%.cc, build/%.o, $(SRCS))

# Ensure the build directory exists
$(shell mkdir -p build)

# Default target
all: $(TARGET)

# Rule to build the target executable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS) $(LDFLAGS)

# Rule to compile source files into object files
build/%.o: src/%.cc
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up build files
clean:
	rm -rf build

install:
	apt update
	apt install libeigen3-dev libsdl2-dev libsdl2-ttf-dev pkg-config

check_pkgs:
	pkg-config --cflags --libs sdl2 
	pkg-config --cflags --libs SDL2_ttf
	pkg-config --cflags --libs eigen3

run: 
	@echo "running..."
	${TARGET}

# Phony targets (not actual files)
.PHONY: all clean check_pkgs install run
