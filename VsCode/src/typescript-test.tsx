//number
let id: number = 1;

//string
let company : string = "my project"

//bool
let isPublish: boolean = true

//var
let x : any = 'hello'

//list
let ids: number[]=[1,2,3,4]

//arraylist
let arr: any[]= [1,2,"name",4]

//tuple
let person : [number, string, boolean] = [1,'name',false]

//2d tuple
let employee: [number,string][] 
employee =[
    [1,"bob"],
    [2,"cathy"],
    [3,"greg"]
    
]

//union 
let pid: string | number
pid = 22
export {};

//object
type User = {
    name: string,
    age : number,
    address: {
        apt:number,
        street:string
    }
}
//object
const user: User = {
    name: 'john',
    age: 33,
    address:{
        apt: 1,
        street: 'abc street'
    }
}



