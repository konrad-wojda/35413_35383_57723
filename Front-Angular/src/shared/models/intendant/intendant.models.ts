import { BaseResponse } from '../base.models';
import { UserDataResponse } from './user.models';

export interface IntendantDataResponse extends UserDataResponse {
  is_main_admin: boolean;
  id_intendant: number;
  id_school: number;
}

export interface IntendantDataResponse extends BaseResponse {
  //
}

export interface IntendantRegisterAdminResponse extends BaseResponse {
  //
}
