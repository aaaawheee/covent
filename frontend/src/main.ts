import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http'; // Provide HttpClient globally
import { LoginComponent } from './app/login/login.component';
import { SignupComponent } from './app/signup/signup.component';

bootstrapApplication(LoginComponent, {
  providers: [
    provideRouter([
      { path: '', component: LoginComponent },
      { path: 'signup', component: SignupComponent },
    ]),
    provideHttpClient()  // Globally provide HttpClient for the app
  ],
}).catch(err => console.error(err));
