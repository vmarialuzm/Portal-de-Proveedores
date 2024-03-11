import { useForm } from "react-hook-form";
import { createUser } from "../api/users.api";
import { useNavigate } from "react-router-dom";

export const SignIn = () => {
  const { 
    register, 
    handleSubmit, 
    formState: { errors },
  } = useForm();
  const navigate = useNavigate();

  const onSubmit = handleSubmit(async data => {
    console.log(data)
    await createUser(data);
    navigate("/login");

  })

  return (
    <div className="max-w-xl mx-auto">
        <h1>Signin</h1>

        <form onSubmit={onSubmit}>
            <input 
                type="email" 
                placeholder="email" 
                className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                {...register("email", { required: true })}
            />
            {errors.email && <span>email is required</span>}

            <input 
                type="text" 
                placeholder="username" 
                className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                {...register("username", { required: true })}
            />
            {errors.username && <span>username is required</span>}

            <input 
                type="password" 
                placeholder="password" 
                className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                {...register("password", { required: true })}
            />
            {errors.password && <span>password is required</span>}

            <select 
                className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                {...register("rol", { required: true })}
            >
                <option value="">Seleccione un rol</option>
                <option value="aprobador">Aprobador</option>
                <option value="colocador">Colocador</option>
            </select>
            {errors.password && <span>password is required</span>}

            <button 
                type="submit"
                className="bg-indigo-500 p-3 rounded-lg block w-full mt-3">
                Save
            </button>
        </form>
    </div>
  )
}