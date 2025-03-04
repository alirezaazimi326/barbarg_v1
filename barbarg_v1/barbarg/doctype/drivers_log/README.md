# Drivers Log

This DocType is used for recording operational logs for drivers.

## Main Features

1. **Driver Link**
   - Links each log to a specific driver
   - Required field
   - Auto-suggests from Drivers DocType

2. **Situation Tracking**
   - Pending: Initial state
   - Processing: In progress
   - Finished: Completed

3. **Status Management**
   - Null: Default state
   - Success: Operation successful
   - Failed: Operation failed

4. **Log Details**
   - JSON field for flexible data storage
   - Supports any valid JSON structure
   - Useful for storing operation-specific data

5. **Timestamp**
   - Automatic timestamp recording
   - Tracks when the log was created

## Example Log Message
```json
{
  "operation": "delivery",
  "location": {
    "lat": 35.7219,
    "lng": 51.3347
  },
  "details": {
    "packages": 3,
    "weight": 150,
    "recipient": "John Doe"
  }
}
```

## Usage Notes
1. Always link logs to a valid driver
2. Use appropriate situation and status combinations
3. Ensure valid JSON format in log messages
4. Logs are automatically deleted when related driver is deleted

## Best Practices
1. Include relevant information in log messages
2. Use consistent JSON structure
3. Update situation and status promptly
4. Regular cleanup of old logs 