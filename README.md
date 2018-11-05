## Cams Biometrics

- API to post attendance from CAMS Biometrics devices to ERPNext
- HR Setting child table to configure device ids, auth token
- On first API call by an Employee, Attendance is created with In time
- On every subsequent call made by the same Employee on the same day will update the Out time(In or Out posted by the device is ignored)
- Every midnight scheduler submits the days Attendance
- On any error, response ok is returned and an Error Log created as well as ToDo is assigned to Employee

#### License

MIT
