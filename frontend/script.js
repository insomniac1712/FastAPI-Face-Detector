const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const processedFrame = document.getElementById("processed-frame");
const roiDataElement = document.getElementById("roi-data");

const ctx = canvas.getContext("2d");

const socket = new WebSocket(
    "ws://localhost:8000/ws/video"
);


async function setupCamera() {

    const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: false
    });

    video.srcObject = stream;
}


setupCamera();


socket.onopen = () => {

    console.log("WebSocket connected");

    setInterval(() => {

        if (!video.videoWidth) return;

        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;

        ctx.drawImage(video, 0, 0);

        const frame = canvas.toDataURL("image/jpeg");

        socket.send(frame);

    }, 150);
};


socket.onmessage = (event) => {

    processedFrame.src = event.data;

};


async function fetchROIData() {

    try {

        const response = await fetch(
            "http://localhost:8000/api/roi"
        );

        const data = await response.json();

        if (data.length > 0) {

            roiDataElement.textContent = JSON.stringify(
                data[0],
                null,
                2
            );

        }

    } catch (error) {

        console.error("ROI fetch failed:", error);

    }
}


setInterval(fetchROIData, 1000);