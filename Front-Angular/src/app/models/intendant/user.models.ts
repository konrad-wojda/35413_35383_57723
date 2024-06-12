import { BaseResponse } from '../base.models';

export interface RegisterResponse extends BaseResponse {
  email: string;
}

export interface LoginResponse extends BaseResponse {
  token: string;
  token_type: string;
  id_user: number;
}

export interface UserDataResponse {
  email: string;
  first_name: string;
  id_user: number;
  is_admin: boolean;
  last_name: string;
}

export interface UserEditResponse {
  detail: string;
}

export interface IntendantDataResponse extends UserDataResponse {
  is_main_admin: boolean;
  id_intendant: number;
  id_school: number;
}
