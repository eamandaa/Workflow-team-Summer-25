# Workflow-team-Summer-25

This repository contains code to generate **synthetic WGS and Imaging datasets** for demonstration and testing purposes.  
The datasets are organised into **raw, processed, and summarised** data, with filenames corresponding to sample IDs.

There are **two main projects** in this repository.

---

## Project 1 – Empty Dataset Generation 

**Project 1** generates the **folder structure and empty files** for WGS and Imaging datasets.  
This is useful for testing workflows, pipelines, and directory layouts without large data files.

### Output for Project 1

#### WGS
- `.fastq` (Raw)
- `.bam` (Processed)
- `.vcf` (Summarised)

#### Imaging
- `.czi` (Raw)
- `.tif` (Processed)
- `.zarr` (Summarised)

All files are empty and named according to the sample ID.

---

## Project 2 – Non-Empty Dataset Generation

**Project 2** generates **non-empty binary files** that mimic real WGS and Imaging datasets.  
The files vary in size to better represent realistic data volumes.

### File size distribution per number of sample
- **25%** in KB  
- **50%** in **1–9 MB**  
- **25%** in **10–30 MB**

Each sample has the **same file size across raw, processed, and summarised** files.

---

### Output for Project 2

Because of the larger file sizes, outputs are **zipped** for easier transport and storage.

#### Imaging
- **1 ZIP file** containing:
  - Raw
  - Processed
  - Summarised folders

#### WGS
- **1 ZIP file** containing:
  - Raw
  - Processed
  - Summarised folders

 #### PatientIDs and SampleIDs mapping 
- **1 CSV file** mapping:
  - `sample_id`
  - `patient_id`

---

## How to Run

### Jupyter Notebook

All notebooks are **independent**, so no other notebooks are required to be run beforehand.

1. Choose the **project**:
   - Project 1 (empty files) 
    Choose if you would like to generate the WGS or Imaging dataset.
   - Project 2 (non-empty binary files). 
    The notebook will generate the WGS and Imaging dataset at the same time.

2. Run **pip install -r requirements.txt** before running Project 2 Notebook. 
Project 1 does not have a requirements.txt

3. Run **only the notebook you need**.

### Python Script - Running the script from the terminal for Project 2

#### Prerequisites
- WSL Ubuntu (or any Linux environment)
- Python 3 installed

1.  Run **pip install -r requirements.txt** to install all libraries needed.

2. Run the script using:
python3 Project_2.py

---

## Notes
- All data generated is **synthetic**.
- No real biological or imaging data is included.
- Designed for demos, MVPs, and workflow testing.