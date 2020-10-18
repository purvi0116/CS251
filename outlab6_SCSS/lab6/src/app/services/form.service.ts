import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Form } from '../userForm';
import { Observable } from 'rxjs';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { FormGroup, FormControl } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class FormService {
  private getUrl = 'https://cs251-outlab-6.herokuapp.com/initial_values/';
  private postUrl = 'https://cs251-outlab-6.herokuapp.com/add_new_feedback/';
  
  constructor(
    private http: HttpClient
  ) { }
  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error.message);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong.
      console.error(
       'Server Side Error: ',error)
    }
    // Return an observable with a user-facing error message.
    return throwError(
      'Something bad happened; please try again later.');
  }

  getForm(): Observable<Form>{
    return this.http.get<Form>(this.getUrl); 
  }
  
  postForm(myform: FormGroup): Observable<Form>{
    
    let formData = new Form('','','','');
    formData.name = myform.get('name').value;
    formData.comment = myform.get('comment').value;
    formData.email = myform.get('email').value;
    formData.feedback = myform.get('feedback').value;
    return this.http.post<Form>(this.postUrl, formData).pipe(
      catchError(this.handleError));
  }
}
