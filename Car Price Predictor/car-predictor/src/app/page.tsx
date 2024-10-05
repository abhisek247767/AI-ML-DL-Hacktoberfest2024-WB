'use client'
import FlickeringGrid from '@/components/magicui/flicker';
import { CheckIcon, ChevronRightIcon } from "lucide-react";
import type { ConfettiRef } from "@/components/magicui/canvas";
import Confetti from "@/components/magicui/canvas";
import { Cover } from "@/components/ui/cover";
import { useState, useEffect, useRef } from 'react';

export default function Home() {
  const confettiRef = useRef<ConfettiRef>(null);
  const [filteredCarModels, setFilteredCarModels] = useState([]);
  const [data, setData] = useState({
    companies: [],
    car_models: [],
    years: [],
    fuel_types: []
  });
  const [formData, setFormData] = useState({
    company: 'Audi',
    car_models: 'Audi A3 Cabriolet',
    year: '2019',
    kilo_driven: '',
    fuel_type: 'Petrol'
  });
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    fetch('https://ml2024.onrender.com/api/data')
      .then(response => response.json())
      .then(data => {
        setData(data);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
      });
  }, []);

  const handleChange = (e:any) => {
    // setFormData({
    //   ...formData,
    //   [e.target.name]: e.target.value
    // });

    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: value
    });

    if (name === 'company') {
      // Filter car models based on the selected company
      setFilteredCarModels(data.car_models.filter((model: string) => model.startsWith(value)));
    }
  };

  const handleSubmit = (e:any) => {
    e.preventDefault();
    console.log(formData)
    fetch('https://ml2024.onrender.com/api/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then(response => response.json())
      .then(data => {
        setPrediction(data.prediction);
      })
      .catch(error => {
        console.error('There was an error making the prediction!', error);
      });
  };

  return (
    <div className='relative h-full w-full bg-[#ebebf1] opacity-80' style={{
      backgroundImage: 'radial-gradient(#444cf7 0.5px, transparent 0.5px), radial-gradient(#444cf7 0.5px, #ebebf1 0.5px)',
      backgroundSize: '20px 20px',
      backgroundPosition: '0 0,10px 10px'
    }}>
        <h1 className='text-4xl md:text-4xl lg:text-6xl font-semibold max-w-7xl mx-auto text-center relative pt-8 z-20 py-4 bg-clip-text text-transparent bg-gradient-to-b from-neutral-800 via-neutral-700 to-neutral-700 dark:from-neutral-800 dark:via-white dark:to-white'><Cover>Car Price Predictor</Cover></h1>
        <form onSubmit={handleSubmit} className="space-y-6 p-8 ">
          <div className="flex flex-col">
            <label className="mb-2 font-semibold text-gray-700">Company:</label>
            <select
              name="company"
              onChange={handleChange}
              className="p-2 border border-slate-800 rounded-md focus:outline-none focus:ring-2 focus:ring-slate-800 bg-transparent"
            >
              {data.companies.map(company => (
                <option key={company} value={company} className='bg-[#ebebf1]'>{company}</option>
              ))}
            </select>
          </div>
          
          <div className="flex flex-col">
            <label className="mb-2 font-semibold text-gray-700">Car Model:</label>
            <select
              name="car_models"
              onChange={handleChange}
              className="p-2 border border-slate-800 rounded-md focus:outline-none focus:ring-2 focus:ring-slate-800 bg-transparent"
            >
              {filteredCarModels.map(model => (
                <option key={model} value={model} className='bg-[#ebebf1]'>{model}</option>
              ))}
            </select>
          </div>
          
          <div className="flex flex-col">
            <label className="mb-2 font-semibold text-gray-700">Year:</label>
            <select
              name="year"
              onChange={handleChange}
              className="p-2 border border-slate-800 rounded-md focus:outline-none focus:ring-2 focus:ring-slate-800 bg-transparent"
            >
              {data.years.map(year => (
                <option key={year} value={year} className='bg-[#ebebf1]'>{year}</option>
              ))}
            </select>
          </div>
          
          <div className="flex flex-col">
            <label className="mb-2 font-semibold text-gray-700">Kilometres Driven:</label>
            <input
              type="number"
              name="kilo_driven"
              onChange={handleChange}
              className="p-2 border border-slate-800 rounded-md focus:outline-none focus:ring-2 focus:ring-slate-800 bg-transparent"
            />
          </div>
          
          <div className="flex flex-col">
            <label className="mb-2 font-semibold text-gray-700">Fuel Type:</label>
            <select
              name="fuel_type"
              onChange={handleChange}
              className="p-2 border border-slate-800 rounded-md focus:outline-none focus:ring-2 focus:ring-slate-800 bg-transparent"
            >
              {data.fuel_types.map(fuel => (
                <option key={fuel} value={fuel} className='bg-[#ebebf1]'>{fuel}</option>
              ))}
            </select>
          </div>

          <button type='submit' className="inline-flex h-12 animate-shimmer items-center justify-center rounded-md border border-slate-800 bg-[linear-gradient(110deg,#000103,45%,#1e2631,55%,#000103)] bg-[length:200%_100%] px-6 font-medium text-slate-300 transition-colors w-full py-2">
                  Predict
                </button>

        </form>

        {prediction && (
          <div className='flex justify-center items-center'>
           <div className="relative flex h-[200px] w-content flex-col items-center justify-center overflow-hidden bg-background">
           <span className="pointer-events-none whitespace-pre-wrap bg-gradient-to-b from-black to-gray-300/80 bg-clip-text text-center text-8xl font-semibold leading-none text-transparent dark:from-white dark:to-slate-900/10">
            {prediction} &#8377;
           </span>
      
           <Confetti
             ref={confettiRef}
             className="absolute left-0 top-0 z-0 size-full"
             onMouseEnter={() => {
               confettiRef.current?.fire({});
             }}
           />
         </div>
         </div>
        )}

    </div>
  );
}
