import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private baseUrl = 'http://localhost:4200/'; // Update with your backend URL

  constructor(private http: HttpClient) {}

  login(email: string, password: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/login`, { email, password });
  }

  signUp(data: { email: string; password: string; userType: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}/signup`, data);
  }

  requestOtp(email: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/otp`, { email });
  }

  resetPassword(email: string, otp: string, newPassword: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/reset-password`, { email, otp, newPassword });
  }
}
