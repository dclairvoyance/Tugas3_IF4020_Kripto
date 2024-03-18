import { useState, useRef, useEffect } from "react";
import { MdLockOutline, MdLockOpen } from "react-icons/md";
import axios from "axios";
import Subpage from "../components/Subpage";
import TextInput from "../components/TextInput";
import FileInput from "../components/FileInput";
import FileOutput from "../components/FileOutput";

const Lazi = () => {
  const [format, setFormat] = useState("text");
  const [fileInputName, setFileInputName] = useState("");
  const [fileOutputName, setFileOutputName] = useState("");
  const [fileInput, setFileInput] = useState(null);
  const [fileURL, setFileURL] = useState(null);
  const [userInput, setUserInput] = useState("");
  const [userOutput, setUserOutput] = useState("");
  const [outputBase64, setOutputBase64] = useState("");
  const outputTextArea = useRef(null);

  const [userKey, setUserKey] = useState("");

  const handleFormat = (format) => {
    setFormat(format);
  };

  const handleUserInput = (textInput) => {
    setUserInput(textInput);
  };
  const handleFileInputChange = (event) => {
    const file = event.target.files[0];
    setFileInputName(file.name);
    setFileInput(file);

    const reader = new FileReader();
    reader.onload = (e) => {
      setUserInput(e.target.result);
    };
    reader.readAsDataURL(file);
  };

  const handleFileOutputChange = (fileNameInput) => {
    setFileOutputName(fileNameInput);
  };

  const testPython = async () => {
    try {
      const response = await axios.get("http://localhost:8080/lazi");
      console.log(response.data.authors);
    } catch (error) {
      console.error("Error: ", error);
      setUserOutput("Error encrypting message.");
    }
  };

  useEffect(() => {
    testPython();
  }, []);

  const encryptAction = async () => {
    if (format === "text") {
      await laziEncryptAction();
    } else {
      await laziFileEncryptMessage();
    }
  };

  const laziEncryptAction = async () => {
    try {
      const response = await fetch("http://localhost:8080/lazi_encrypt", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userInput, userKey }),
      });
      const data = await response.json();
      const decoded_data = atob(data.message);
      setUserOutput(decoded_data);
      setOutputBase64(data.message);
    } catch (error) {
      console.error("Error: ", error);
      setUserOutput("Error encrypting message.");
    }
  };

  const laziFileEncryptMessage = async () => {
    try {
      const formData = new FormData();
      formData.append("file", fileInput);
      formData.append("userKey", userKey);

      const response = await fetch("http://localhost:8080/lazi_file_encrypt", {
        method: "POST",
        body: formData,
      });

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      setFileURL(url);

      const reader = new FileReader();
      reader.onload = function (event) {
        setUserOutput(event.target.result);
      };

      reader.readAsText(blob, "ASCII");

      const reader2 = new FileReader();
      reader2.onload = function (event) {
        const base64Data = event.target.result.split(",")[1];
        setOutputBase64(base64Data);
      };

      reader2.readAsDataURL(blob);
    } catch (error) {
      console.error("Error:", error);
      setUserOutput("Error downloading file.");
    }
  };

  const decryptAction = async () => {
    if (format === "text") {
      await laziDecryptAction();
    } else {
      await laziFileDecryptMessage();
    }
  };

  const laziDecryptAction = async () => {
    try {
      const response = await fetch("http://localhost:8080/lazi_decrypt", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userInput, userKey }),
      });
      const data = await response.json();
      const decoded_data = atob(data.message);
      setUserOutput(decoded_data);
      setOutputBase64(data.message);
    } catch (error) {
      console.error("Error: ", error);
      setUserOutput("Error encrypting message.");
    }
  };

  const laziFileDecryptMessage = async () => {
    try {
      const formData = new FormData();
      formData.append("file", fileInput);
      formData.append("userKey", userKey);

      const response = await fetch("http://localhost:8080/lazi_file_decrypt", {
        method: "POST",
        body: formData,
      });

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      setFileURL(url);

      const reader = new FileReader();
      reader.onload = function (event) {
        setUserOutput(event.target.result);
      };

      reader.readAsText(blob, "ASCII");

      const reader2 = new FileReader();
      reader2.onload = function (event) {
        const base64Data = event.target.result.split(",")[1];
        setOutputBase64(base64Data);
      };

      reader2.readAsDataURL(blob);
    } catch (error) {
      console.error("Error:", error);
      setUserOutput("Error downloading file.");
    }
  };

  const handleFileOutputSubmit = () => {
    const element = document.createElement("a");
    const file = new Blob([outputTextArea.current.value], {
      type: "text/plain",
    });

    if (format === "file") {
      element.href = fileURL;
    } else {
      element.href = URL.createObjectURL(file);
    }

    element.download = fileOutputName ? fileOutputName : "encrypted";
    document.body.appendChild(element); // Firefox
    element.click();
  };

  return (
    <>
      <div className="p-2 bg-primary_1 rounded-md">
        {/* format picker */}
        <Subpage
          currentVariable={format}
          handleVariable={handleFormat}
          variables={["text", "file"]}
        />

        {/* input/output */}
        <div className="flex">
          {/* input */}
          <div className="basis-5/12 flex-col mx-1">
            <h2 className="h-8 items-center ml-1 mb-4 flex text-lg font-semibold text-white">
              Input
            </h2>
            {/* text input */}
            {format === "text" && (
              <TextInput handleOnChangeParent={handleUserInput} />
            )}

            {/* file input */}
            {format === "file" && (
              <FileInput
                handleOnChangeParent={handleFileInputChange}
                fileName={fileInputName}
              />
            )}
          </div>

          {/* key */}
          <div className="basis-2/12 flex-col mx-1">
            <h2 className="h-8 items-center ml-1 mb-4 flex text-lg font-semibold text-white">
              Key
            </h2>
            <div className="flex-col mx-1 mb-3">
              <input
                id="key"
                className="w-full p-1.5 text-lg text-white bg-primary_2 rounded-md border border-primary_3 focus:ring-blue-50 mr-2"
                placeholder="Key"
                value={userKey}
                onChange={(e) => setUserKey(e.target.value)}
              ></input>
            </div>
            <div className="lg:flex">
              <button
                onClick={encryptAction}
                className="bg-primary_2 hover:bg-primary_3 border-primary_3 text-secondary px-2 py-1.5 my-1 lg:mr-1 rounded flex items-center mx-auto"
              >
                <MdLockOutline size="16" />
                <span className="text-sm">Encrypt</span>
              </button>
              <button
                onClick={decryptAction}
                className="bg-primary_2 hover:bg-primary_3 border-primary_3 text-secondary px-2 py-1.5 my-1 lg:ml-1 rounded flex items-center mx-auto"
              >
                <MdLockOpen size="16" />
                <span className="text-sm">Decrypt</span>
              </button>
            </div>
          </div>

          {/* output */}
          <div className="basis-5/12 flex-col mx-1">
            <div className="md:flex md:justify-between mb-1">
              <h2 className="h-8 items-center ml-1 flex text-lg font-semibold text-white">
                Output
              </h2>
              {/* download as txt file */}
              <FileOutput
                handleOnChangeParent={handleFileOutputChange}
                handleOnSubmitParent={handleFileOutputSubmit}
              />
            </div>
            <textarea
              readOnly
              id="output"
              ref={outputTextArea}
              rows="5"
              className="w-full p-2 text-lg text-white bg-primary_2 rounded-md border border-primary_3"
              value={userOutput}
            ></textarea>
            <h2 className="mb-1 h-8 items-center ml-1 flex text-lg font-semibold text-white">
              Base64
            </h2>
            <textarea
              readOnly
              id="output"
              rows="5"
              className="w-full p-2 text-lg text-white bg-primary_2 rounded-md border border-primary_3"
              value={outputBase64}
            ></textarea>
          </div>
        </div>
      </div>
    </>
  );
};

export default Lazi;
