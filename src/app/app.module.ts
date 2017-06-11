import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MdButtonModule, MdSliderModule, MdInputModule, MdCardModule } from '@angular/material';
import { ColorPickerModule } from 'ngx-color-picker';
import 'hammerjs';

// import { AngularMD } from "./angular.md.module";
import { AppComponent } from './app.component';

import { ServiceService } from "./service.service";

@NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule, BrowserAnimationsModule, HttpModule,
        MdButtonModule, MdSliderModule, MdInputModule, MdCardModule
        // AngularMD
        , ColorPickerModule
    ],
    providers: [ServiceService],
    bootstrap: [AppComponent]
})
export class AppModule { }
