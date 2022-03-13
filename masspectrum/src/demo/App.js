/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';
import ReactDOM from "react-dom";
import {PivotData} from "react-pivottable/Utilities";

import { masspectrum } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.state = {
            value: ''
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <masspectrum
                    setProps={this.setProps}
                    {...this.state}
                />
            </div>
        )
    }
}

export default App;
