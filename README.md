# BarBarg - Driver and Log Management System

A system designed for managing driver information and their operational logs.

## DocTypes

### 1. Drivers
This DocType is used to store driver information.

#### Main Fields:
- **Personal Information**
  - User Name (Required)
  - Password (Required)

- **Sender and Receiver Information**
  - Sender Full Name
  - Sender Phone Number
  - Receiver Full Name
  - Receiver Phone Number

- **Vehicle Information**
  - IR Code (2 digits)
  - License Plate Letter (Select from Persian letters)
  - Middle 3 digits
  - Left 2 digits
  - Full Plate (Auto-generated)

- **Geolocation**
  - Origin Latitude & Longitude
  - Destination Latitude & Longitude

- **Cargo Information**
  - Product Name
  - Weight
  - Number of Packages
  - Packaging Type
  - Cargo Value (in Rials)
  - Insurance Status

### 2. Drivers Log
This DocType is used to record operational logs for drivers.

#### Main Fields:
- **Driver** - Link to Drivers DocType
- **Situation**
  - Pending
  - Processing
  - Finished
- **Status**
  - Null
  - Success
  - Failed
- **Log Message** - JSON field for storing log details
- **Timestamp** - Log creation time

## Important Notes

1. **Record Deletion**:
   - When deleting a driver, all related logs are automatically deleted
   - Before deleting a driver, ensure you don't need their logs anymore

2. **Log Recording**:
   - Logs are recorded independently
   - Each log must be linked to a driver
   - Log message can store any JSON data

3. **License Plate**:
   - Full plate is automatically generated from components
   - Format: `IR Code | Middle 3 digits Letter Left 2 digits`

## How to Use

1. **Creating a New Driver**:
   - Go to Drivers section
   - Click "New"
   - Fill in required information
   - Click "Save"

2. **Recording a New Log**:
   - Go to Drivers Log section
   - Click "New"
   - Select the driver
   - Set situation and status
   - Enter log message in JSON format
   - Click "Save"

## Requirements
- Frappe Framework
- MariaDB/MySQL
- Python 3.x