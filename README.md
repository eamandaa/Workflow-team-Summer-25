# Workflow-team-Summer-25

This repository contains code to generate **synthetic WGS and Imaging datasets** for demonstration and testing purposes.  
The datasets are organised into **raw, processed, and summarised** data, with filenames corresponding to sample IDs.

There are **two main projects** in this repository.

---

## Project 1 – Empty Dataset Generation (MVP)

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

### File size distribution per sample
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
- **1 CSV file** mapping:
  - `sample_id`
  - `patient_id`

#### WGS
- **1 ZIP file** containing:
  - Raw
  - Processed
  - Summarised folders
- **1 CSV file** mapping:
  - `sample_id`
  - `patient_id`

---

## How to Run

All notebooks are **independent**.

1. Choose the **project**:
   - Project 1 (empty files)
   - Project 2 (non-empty binary files)

2. Choose the **dataset**:
   - WGS
   - Imaging

3. Run **only the notebook you need**.

No other notebooks are required to be run beforehand.

---

## Notes
- All data generated is **synthetic**.
- No real biological or imaging data is included.
- Designed for demos, MVPs, and workflow testing.