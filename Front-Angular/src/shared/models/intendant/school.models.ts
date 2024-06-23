import { BaseResponse } from '../base.models';

export interface SchoolData {
  name_of_school: string;
  post_code: number;
  street_name: string;
  street_number: number;
}

export interface SchoolCreateData extends SchoolData {
  token: string;
}

export interface SchoolCreateResponse extends BaseResponse {
  id_school: string;
}
