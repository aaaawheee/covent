import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-signup',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
})
export class SignupComponent {
  email: string = '';
  password: string = '';
  userType: string = 'SPONSOR'; // Default value

  constructor() {}

  onSignUp(): void {
    // Example logic for sign-up
    console.log('Sign Up Form Data:', {
      email: this.email,
      password: this.password,
      userType: this.userType,
    });

    // You can replace this with an HTTP request to the backend
    alert('Sign Up successful!');
  }
}