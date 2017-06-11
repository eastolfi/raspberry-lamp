import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Rx';

// Import RxJs required methods
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class ServiceService {
    private URL = "http://0.0.0.0:3000"
    
    constructor(private http: Http) { }

    setColorHex(color: string): Observable<string> {
        // return this.http.get(`${this.URL}/color/${color}`)
        return this.http.get("http://raspberry-lamp-eastolfi.c9users.io:3000/color/asd")
            .map((res:Response) => {
                debugger;
                return res.json()
            })
            .catch((error: any) => {
                debugger;
                return Observable.throw(error.json().error || 'Server error')
            });
    }
}
