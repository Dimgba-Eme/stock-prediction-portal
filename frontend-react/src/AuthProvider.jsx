import { useState, useContext, createContext } from 'react'

const AuthContext = createContext()

const AuthProvider = ({ children }) => {
    // !! prevents the entire access token to be retrieved raw 
    const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('accessToken'));

    return (
        <AuthContext.Provider value={{ isLoggedIn, setIsLoggedIn }}>
            {children}
        </AuthContext.Provider>
    )
}

export default AuthProvider

export {AuthContext};