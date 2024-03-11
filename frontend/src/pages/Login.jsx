import { useState } from "react";
import { useForm } from "react-hook-form";
import { loginUser } from "../api/users.api";
import { useNavigate } from "react-router-dom";

export const Login = () => {

    const {
        register,
        handleSubmit,
        formState: { errors }
    } = useForm();
    const navigate = useNavigate();
    const [error, setError] = useState("");

    const onSubmit = handleSubmit(async data => {
        try {
            await loginUser(data);
            navigate('/home');
        } catch (error) {
            setError("Invalid email or password. Please try again.");
        }
    });

    return (
        <div className="max-w-xl mx-auto">
            <h1>Login</h1>

            <form onSubmit={onSubmit}>
                <input 
                    type="email" 
                    placeholder="email" 
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                    {...register("email", { required: true })}
                />
                {errors.email && <span>Email is required</span>}

                <input 
                    type="password" 
                    placeholder="password" 
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                    {...register("password", { required: true })}
                />
                {errors.password && <span>Password is required</span>}

                {/* Muestra el mensaje de error si existe */}
                {error && <span className="text-red-500">{error}</span>}
                
                <button 
                    type="submit"
                    className="bg-indigo-500 p-3 rounded-lg block w-full mt-3">
                    Iniciar Sesión
                </button>
            </form>
        </div>
    )
}