import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MdButtonModule, MdSliderModule, MdInputModule, MdCardModule } from '@angular/material';
import { ColorPickerModule } from 'ngx-color-picker';
import 'hammerjs';

// import { AngularMD } from "./angular.md.module";
import { AppComponent } from './app.component';

@NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule, BrowserAnimationsModule,
        MdButtonModule, MdSliderModule, MdInputModule, MdCardModule
        // AngularMD
        , ColorPickerModule
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
