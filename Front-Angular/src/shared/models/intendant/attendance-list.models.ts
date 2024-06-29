export interface AttendanceListResponse {
  id_student: number;
  data: [string, number];
}

export interface AttendanceListRequest {
  token: string;
  id_school: number;
  date: string;
  attendance_list: AttendanceList[];
}

export interface AttendanceList {
  id_student: number;
  id_meal_type: number[];
}
