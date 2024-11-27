import { useState } from 'react'
import './App.css'
import Navbar from './Navbar'
import { notes } from './notes'

type Note = {title: string, content: string}

function Note({title, content}: Note) {

  const [flipped, setFlipped] = useState(false)
  const [count, setCount] = useState(0)
  const [example, setExample] = useState<Note>({title: "this", content: "that"})


  setExample({...example})

  return (
    <div className='note' onClick={()=>{
      setFlipped(!flipped)
      setCount(count + 1)
      console.log("hello")
      }}>
      <h1>{count}</h1>
      <h1>
        {title}
      </h1>
      {!flipped && <p>{content}</p>}

    </div>
 
  )
}

export default function App() {
  return (
    <>
    
      <Navbar></Navbar>
      
      <div id="notes-container">
        {notes.map((x)=> <Note title={x.title} content={x.content}></Note>)}
      </div>
      
    </>
  )
}