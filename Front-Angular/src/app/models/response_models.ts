export interface RegisterResponse {
  changed: boolean;
  status_code: number;
  email?: string;
}

export interface UserDataResponse {
  email: string;
  first_name: string;
  flat_number: number;
  is_active: boolean;
  is_admin: boolean;
  is_employee: boolean;
  last_name: string;
  post_code: number;
  street_name: string;
  street_number: number;
  telephone: number;
  user_id: number;
}

export interface UserAdressResponse {
  email: string;
  last_name: string;
  first_name: string;
  telephone: number;
  post_code: number;
  street_name: string;
  street_number: number;
  flat_number: number;
}
