// import style from './wrapper.module.css'
import { Container } from 'react-bootstrap';
import NaviBar from '../navibar/NaviBar';
import Sidebar from '../sidebar/sidebar';
import './wrapper.css';

function Wrapper(){
    return <>
        <div className='wrapper'>
            <Sidebar />
            <div className='main'>
                <NaviBar />
                <Container/>
                
            </div>
        </div>
    </>
}

export default Wrapper
