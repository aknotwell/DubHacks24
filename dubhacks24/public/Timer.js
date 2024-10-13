class Timer extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            name:"",
            appVersion:'',
        }
    }
    render(){
        return(
            <>
            <h2>Hello World</h2>
            <button>timer</button>
            </>
        )
    }
}