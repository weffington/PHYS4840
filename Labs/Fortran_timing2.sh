#!/bin/bash

# Measure compilation time
echo "Compiling oddball.f90..."
start_compile=$(date +%s.%N)
gfortran oddball.f90 -o oddball.exe
end_compile=$(date +%s.%N)
compile_time=$(echo "$end_compile - $start_compile" | bc)

echo "Running oddball.exe..."
# Measure execution time
start_exec=$(date +%s.%N)
./oddball.exe
end_exec=$(date +%s.%N)
exec_time=$(echo "$end_exec - $start_exec" | bc)

echo "Compilation time: $compile_time seconds"
echo "Execution time: $exec_time seconds"