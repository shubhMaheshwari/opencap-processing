# Use Ubuntu 22.04 as base image
FROM ubuntu:22.04

# Set the working directory
WORKDIR /opencap-processing

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    git \
    build-essential \
    libopenblas-base \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

# Update PATH environment variable
ENV PATH=/opt/conda/bin:$PATH

# Create conda environment with Python 3.11
RUN conda create -y -n opencap-processing python=3.11

# Activate the environment and install OpenSim
RUN /opt/conda/bin/conda run -n opencap-processing conda install -y -c opensim-org opensim=4.5=py311np123

# Clone the opencap-processing repository
RUN git clone https://github.com/shubhMaheshwari/opencap-processing.git .

# Install required Python packages
RUN /opt/conda/bin/conda run -n opencap-processing pip install --no-cache-dir -r requirements.txt

# Install OpenBLAS libraries (already installed above)
# RUN apt-get update && apt-get install -y libopenblas-base

# Expose ports if needed (uncomment if your application uses networking)
# EXPOSE 8000

# Set the command to activate the environment and start the application
CMD ["conda", "run", "--no-capture-output", "-n", "opencap-processing", "python", "Examples/example_walking_opensimAD.py"]