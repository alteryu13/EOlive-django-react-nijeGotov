import React, { Component } from 'react';
import {  FormGroup, Label, Input } from 'reactstrap';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import axios from 'axios';
import './static/style.css';

export class OPGinfo extends Component {
    constructor(props){
        super(props);
        this.state={
            katastar:'',
            naselje:'',
            povrsina:'',
            naziv_gosp:'',
            id:''
        }
    }

    handleClick(event){
        axios.post('http://127.0.0.1:8000/api/Evidencija/create/', {
            katastar: this.katastar,
            naselje: this.naselje,
            povrsina: this.povrsina,
            naziv_gosp: this.naziv_gosp,
        }).then(response => {
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        })
    }

    render() {
        let errorM = null;
        if(this.props.error){
        errorM = (
            <p>{this.props.error.message}</p>
        );
        }
        return (
            <div>
                {errorM}
                <Form>
                    <FormGroup className="Formfield">
                        <Label className="Labelfield" for="katastar"></Label>
                        <Input type="text" name="katastar" className="FormLogin" id="katastar" placeholder="Unesite katastarsku česticu" onChange = {(event) => this.setState({katastar: event.target.value})} />
                    </FormGroup>
                    <FormGroup className="Formfield">
                        <Label for="naselje"></Label>
                        <Input type="text" name="naselje" id="naselje" placeholder="Unesite naselje" onChange = {(event) => this.setState({naselje: event.target.value})}/>
                    </FormGroup>
                    <FormGroup className="Formfield">
                        <Label for="povrsina"></Label>
                        <Input type="text" name="povrsina"  id="povrsina" placeholder="povrsina" onChange = {(event) => this.setState({povrsina: event.target.value})} />
                    </FormGroup>
                    <FormGroup className="Formfield">
                        <Label for="naziv_gosp"></Label>
                        <Input type="text" name="naziv_gosp"  id="naziv_gosp" placeholder="Unesite naziv OPG-a" onChange = {(event) => this.setState({naziv_gosp: event.target.value})} />
                    </FormGroup>
                    <FormGroup className="Formfield">
                        <Button type="submit" variant="success" className="button_p" onClick={(event) => this.handleClick(event)}>Potvrsi unos</Button>
                    </FormGroup>
                </Form>
            </div>
        )
    }
}




export default OPGinfo;