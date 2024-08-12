import React, { useState } from 'react';
import { AlertCircle } from 'lucide-react';
import "../components/styles/iris.css"
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import David from "../components/styles/Gardener.png"
import Image1 from "../components/styles/image1.png"
import Image2 from "../components/styles/image2.png"
import Image3 from "../components/styles/image3.png"
// import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';

const API_URL = '/api';

const IrisClassification = () => {
  const [measurements, setMeasurements] = useState({
    sepal_length: '',
    sepal_width: '',
    petal_length: '',
    petal_width: '',
  });
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setMeasurements(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`http://127.0.0.1:8000/predict`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(measurements),
        
      });
      if (!response.ok) throw new Error('Failed to get prediction');
      const data = await response.json();
      setPrediction(data);
      setError(null);
      setMeasurements({
        sepal_length: '',
        sepal_width: '',
        petal_length: '',
        petal_width: '',
      });
      toast.success(`The predicted Iris species is: ${data.class_label}`);
    } catch (err) {
      setError('An error occurred while fetching the prediction.');
      setPrediction(null);
    }
  };

  return (
    <div className="iris-main">
      <ToastContainer 
      position='top-center'
      closeOnClick

      rtl={false}
      />
      <nav>
        <h1 className="text-3xl font-bold mb-6">Iris Flower Classification</h1>
        <a href="#enter"><button>Get Prediction</button></a>
      </nav>
      
      <div className="iris-text">
        <div className="image">
          <img src={David} alt="David the Gardener" className="w-24 h-24 rounded-full mr-4" />
        </div>
        <div className="text">
          <h2 className="text-xl font-semibold mb-4">Meet David the Gardener</h2>
          <p className="text-gray-700">
            Hello there! I'm David, your friendly neighborhood gardener with a passion for all things green and blooming. Today, I'm excited to introduce you to one of my favorite flowers—the beautiful Iris.
          </p>
          <p>
            Iris flowers come in a variety of colors and shapes, but did you know that there are three main species? These are the Iris Setosa, Iris Versicolor, and Iris Virginica. Each species has its own unique characteristics, making them both fascinating and sometimes tricky to identify.
          </p>
          <p>
            But don’t worry! I’ve got just the thing to help you out. With the power of Machine Learning, I’ve trained a model that can identify these three types of Iris flowers with remarkable accuracy. Just enter the features of your flower, and let the model do the rest. It’s like having your very own gardening assistant!
          </p>
        </div>
      </div>

      <div className="images">
        <div className="flower">
          <img src={Image1} alt="" />
          <h1>Iris Setosa</h1>
        </div>
        <div className="flower">
          <img src={Image2} alt="" />
          <h1>Iris Versicolor</h1>
        </div>
        <div className="flower">
          <img src={Image3} alt="" />
          <h1>Iris Virginica</h1>
        </div>
      </div>

      <div className="how">
        <h2 className="text-xl font-semibold mb-4">How it works</h2>
        <p className="mb-4">To identify the type of Iris flower you have, our model needs some specific information about the flower. Don't worry, it's easy! Just measure and enter the following details:</p>
        <ul className="list-disc pl-6 mb-4">
          <li><strong>Sepal Length (sepal_length):</strong> The length of the sepal, which is the outer part of the flower that protects the petals. Measure it in centimeters.</li>
          <li><strong>Sepal Width (sepal_width):</strong> The width of the sepal, again in centimeters. This helps our model understand the size and shape of the flower.</li>
          <li><strong>Petal Length (petal_length):</strong> The length of the petal, which is the colorful part of the flower. Measure this in centimeters too.</li>
          <li><strong>Petal Width (petal_width):</strong> The width of the petal, also in centimeters. This is important for distinguishing between different Iris species.</li>
        </ul>
      </div>

      <form onSubmit={handleSubmit} className="enter" id='enter'>
        <h2 className="text-xl font-semibold mb-4">Get Prediction</h2>
        <p>After entering the required measurements—Sepal Length, Sepal Width, Petal Length, and Petal Width—please make sure you've input only numbers. Once everything is filled out, simply click the "Predict" button to get your prediction. 
          The model will then analyze your inputs and tell you which Iris species you're looking at!</p>
        <div className="inputs">
          <input 
            type="number" 
            placeholder='Sepal Length (cm)' 
            name='sepal_length'
            onChange={handleInputChange}
            value={measurements.sepal_length}
          />
          <input 
            type="number" 
            placeholder='Sepal Width (cm)' 
            name='sepal_width'
            onChange={handleInputChange}
            value={measurements.sepal_width}
          />
          <input 
            type="number" 
            placeholder='Petal Length (cm)' 
            name='petal_length'
            onChange={handleInputChange}
            value={measurements.petal_length}
          />
          <input 
            type="number" 
            placeholder='Petal Width (cm)' 
            name='petal_width'
            onChange={handleInputChange}
            value={measurements.petal_width}
          />
        </div>
        <div>
          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >
            Get Prediction
          </button>
        </div>
        {prediction && (
        <h1>The predicted Iris species is: {prediction.class_label}</h1>
        )}
      </form>

     

      {error && (
        <div className="error">
          <AlertCircle className="h-4 w-4" />
          <strong>Error:</strong> {error}
        </div>
      )}
    </div>
  );
};

export default IrisClassification;
