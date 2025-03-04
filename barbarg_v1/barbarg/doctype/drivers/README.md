# Drivers

This DocType is used for managing driver information.

## Main Features

1. **Auto Naming**
   - Format: `DRV.#####`
   - Example: `DRV00001`

2. **Personal Information**
   - Username and password are required
   - Support for sender and receiver details

3. **License Plate Management**
   - Separate input for plate components
   - Automatic full plate generation
   - Support for all Persian letters

4. **Geolocation**
   - Store origin and destination coordinates
   - 6 decimal precision

5. **Cargo Information**
   - Product details management
   - Cargo insurance support

## Important Methods

### `validate()`
- Checks for username and password
- Logs for debugging

### `generate_full_plate()`
- Combines plate components
- Generates formatted full plate

### `on_trash()`
- Automatically deletes related logs
- Records result in system log

## Security Notes
1. Password is hidden in logs
2. Only system manager can delete records
3. Deleting a driver removes all related logs

## Debug Log JSON Example
```json
{
  "user_name": "driver1",
  "password": "***",
  "plate_info": {
    "left": "22",
    "char": "ب",
    "middle": "333",
    "right": "88"
  }
}
``` 