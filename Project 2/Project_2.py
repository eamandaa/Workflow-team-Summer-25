#!/usr/bin/env python
# coding: utf-8

# # Generate non-empty files of WGS and Imaging dataset of raw, processed and summarised files for 200 patients with 1 sample each. 

# ## Import libraries

# In[1]:


import os
import random
import math
import matplotlib.pyplot as plt
import string


# In[ ]:


# Generate the WGS and Imaging datasets
num_samples = 200

# Base paths
wgs_base = "WGS"
img_base = "Imaging"

# Folder structures
datasets = {
    "WGS": {
        "base": wgs_base,
        "suffix": "AGRF",
        "extensions": [".fastq", ".bam", ".vcf"]
    },
    "Imaging": {
        "base": img_base,
        "suffix": "CDI",
        "extensions": [".czi", ".tif", ".zarr"]
    }
}

# Size categories
categories = ["KB", "1-9MB", "10-30MB"]

def assign_category(index, total):
    if index < total * 0.25:
        return "KB"
    elif index < total * 0.75:
        return "1-9MB"
    else:
        return "10-30MB"

def base_size_for_category(category):
    """Base size represents the RAW file size for that sample category."""
    if category == "KB":
        return random.randint(10 * 1024, 900 * 1024)
    elif category == "1-9MB":
        return random.randint(1 * 1024 * 1024, 9 * 1024 * 1024)
    else:
        return random.randint(10 * 1024 * 1024, 30 * 1024 * 1024)

def stage_sizes_from_raw(raw_size):
    """Produce different sizes for Raw / Processed / Summarised """
    # Processed: 55% - 90% of raw
    processed = int(raw_size * random.uniform(0.55, 0.90))

    # Summarised: 0.2% - 5% of raw
    summarised = int(raw_size * random.uniform(0.002, 0.05))

    # Make sure the file is not too small and following the right logic
    summarised = max(4 * 1024, summarised)          # at least 4KB
    processed = max(summarised + 1024, processed)   # processed > summarised
    raw = max(processed + 1024, raw_size)           # raw > processed

    return raw, processed, summarised

def write_binary_file(path, size_bytes, chunk_size=1024 * 1024):
    remaining = size_bytes
    with open(path, "wb") as f:
        while remaining > 0:
            chunk = min(chunk_size, remaining)
            f.write(os.urandom(chunk))
            remaining -= chunk

# Create folders
for ds in datasets.values():
    for sub in ["Raw", "Processed", "Summarised"]:
        os.makedirs(os.path.join(ds["base"], sub), exist_ok=True)

# Generate data
for i in range(num_samples):
    category = assign_category(i, num_samples)

    # Choose a base RAW size per sample 
    raw_size = base_size_for_category(category)

    # Derive different sizes for each stage
    raw_bytes, processed_bytes, summarised_bytes = stage_sizes_from_raw(raw_size)

    for name, ds in datasets.items():
        sample_id = f"XY{i+1:03d}-{ds['suffix']}"
        paths_and_sizes = [
            (os.path.join(ds["base"], "Raw", f"{sample_id}{ds['extensions'][0]}"), raw_bytes),
            (os.path.join(ds["base"], "Processed", f"{sample_id}{ds['extensions'][1]}"), processed_bytes),
            (os.path.join(ds["base"], "Summarised", f"{sample_id}{ds['extensions'][2]}"), summarised_bytes),
        ]

        for path, size_bytes in paths_and_sizes:
            write_binary_file(path, size_bytes)

print("WGS and Imaging datasets generated successfully")



# In[3]:


#Create a csv file to map the patientid to the sampleid
import csv

output_csv = "patient_sample_mapping.csv"

with open(output_csv, "w", newline="") as f:
    writer = csv.writer(f)
    
    # Header
    writer.writerow(["PatientID", "WGS_SampleID", "Imaging_SampleID"])
    
    # Rows
    for i in range(1, num_samples + 1):
        patient_id =  f"PatientID{i:03d}_DiseaseX"
        wgs_sample_id = f"XY{i:03d}-AGRF"
        imaging_sample_id = f"XY{i:03d}-CDI"
        
        writer.writerow([patient_id, wgs_sample_id, imaging_sample_id])

print("CSV file created:", output_csv)


# In[4]:


#Zip the Imaging output datafiles
import shutil

# Folder to zip
folder_to_zip = "Imaging"

# Output zip file name 
output_zip = "Imaging"

# Create the zip
shutil.make_archive(output_zip, "zip", folder_to_zip)

print("Imaging folder zipped successfully.")


# In[5]:


#Zip the WGS output datafiles
import shutil

# Folder to zip
folder_to_zip = "WGS"

# Output zip file name 
output_zip = "WGS"

# Create the zip
shutil.make_archive(output_zip, "zip", folder_to_zip)

print("WGS folder zipped successfully.")

