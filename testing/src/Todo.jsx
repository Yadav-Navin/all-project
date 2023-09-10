import React,{ useState } from 'react'

const Todo = () => {
    const obj = [
        { id: 0, name: "Navin", age: 21 },
        { id: 1, name: "saurabh", age: 22 },
        { id: 2, name: "shubham", age: 23 },
        { id: 3, name: "vishal", age: 24 }]

    const [Data, setData] = useState(obj);
    const clearData = () => {
        return (
            setData([])
        )
    }
    const deleteData = (id) => {
        const newArray = Data.filter((curEle) => {
            return curEle.id !== id;
        })
        setData(newArray)
    }

    return (
        <div className="App-header">
            <h1>Todo List</h1>
            {
                Data.map((curEle) => {
                    return (<p className='btn' key={curEle.id}>Id is : {curEle.id} and Name is : {curEle.name} and age is : {curEle.age} <button className='clear' onClick={() => deleteData(curEle.id)}>Delete</button></p>)
                })
            }
            <button className='clear' onClick={clearData}>clear</button>
        </div>
    );

}

export default Todo
