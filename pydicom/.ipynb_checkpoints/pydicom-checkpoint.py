import pydicom

# Load a sample DICOM file
ds = pydicom.dcmread("sample.dcm")

# Print basic info
print(ds.PatientName)
print(ds.Modality)
print(ds.StudyDate)
