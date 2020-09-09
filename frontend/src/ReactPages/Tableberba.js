import React from 'react';
import MaterialTable from 'material-table';
import axios from "axios";


class Berba extends React.Component {
    constructor() {
        super();
        this.state = {
            columns: [
                { title: 'Vrsta Maslina', field: 'vrstamaslina' },
                { title: 'Datum', field: 'datumb' },
                { title: 'Katastarke čestice', field: 'katcest' },
                { title: 'Kolicina Ubrano u Kg', field: 'kolicinaubrano' },
                { title: 'Doprinos Ulja', field: 'doprinosulja' },
            ],
            tabledata: [{
                vrstamaslina: '',
                datumb: '',
                katcest: '',
                kolicinaubrano: '',
                doprinosulja: '',
            }],
        };
    }
    render() {
        return (
            <div>
                <MaterialTable 
                    title="Berba"
                    columns={this.state.columns}
                    data={query =>
                        new Promise((resolve, reject) => {
                          let url = 'http://127.0.0.1:8000/api/Berba';
                          axios.get(url, {
                                responseType: 'json'
                            }).then((response) => {
                              resolve({
                                data: response.data,
                                page: response.currentPage - 1,
                                totalCount: response.totalRows,
                              });
                            });
                        })
                      }
                    editable={{
                        onRowAdd: newData =>
                        new Promise(resolve => {
                            setTimeout(() => {
                                resolve();
                                this.setState(prevState => {
                                const data = [prevState.data];
                                data.push(newData);
                                return { prevState, data };
                                });
                                }, 600);
                                axios.post('http://127.0.0.1:8000/api/Berba/create/', {
                                   tabledata: newData,
                                }).then(response => {
                                    console.log(response)
                                });
                            }),
                        onRowUpdate: (newData, oldData) =>
                            new Promise(resolve => {
                                setTimeout(() => {
                                    resolve();
                                    if (oldData) {
                                        this.setState(prevState => {
                                            const data = [...prevState.data];
                                            data[data.indexOf(oldData)] = newData;
                                            return { ...prevState, data };
                                        });
                                    }
                                }, 600);
                            }),
                        onRowDelete: oldData =>
                            new Promise(resolve => {
                                setTimeout(() => {
                                    resolve();
                                    this.setState(state => {
                                        const data = [...state.data];
                                        data.splice(data.indexOf(oldData), 1);
                                        return { ...state, data };
                                    });
                                }, 600);
                            }),
                    }}
                />
            </div>
        );
    }
}



  export default Berba;