import { Component } from '@angular/core';

import { ServiceService } from "./service.service";

function hexToR(h) {return parseInt((cutHex(h)).substring(0,2),16)}
function hexToG(h) {return parseInt((cutHex(h)).substring(2,4),16)}
function hexToB(h) {return parseInt((cutHex(h)).substring(4,6),16)}
function cutHex(h) {
    if (h.length === 4) {
        h = `#${h.charAt(1)}${h.charAt(1)}${h.charAt(2)}${h.charAt(2)}${h.charAt(3)}${h.charAt(3)}`
    }
    return (h.charAt(0)=="#") ? h.substring(1,7) : h
}

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    title = 'app';
    
    color: string = "#FF00FF";
    bright: number = 5;
    
    constructor(private service: ServiceService) { }
    
    onBrightChanged(event) {
        this.bright = event.value;
    }
    
    update() {
        // alert(`Color: ${this.color} / ${hexToR(this.color)}, ${hexToG(this.color)}, ${hexToB(this.color)} and brightness: ${this.bright / 10}`);
        this.service.setColorHex(this.color)
            .subscribe(
                result => {
                    debugger;
                    console.log(result);
                },
                err => {
                    console.log(err);
                }
            );
    }
}
