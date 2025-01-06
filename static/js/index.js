import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

// Your Three.js code here...

// Set up your scene, camera, and renderer
console.log(THREE);

// Create the Scene
const scene = new THREE.Scene();

// Create the Camera
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);

// Create the Renderer
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Initialize OrbitControls
const controls = new OrbitControls(camera, renderer.domElement);

// Add Hemisphere Light
const hemiLight = new THREE.HemisphereLight(0x87CEEB, 0x4B0082, 1.6); // Sky color, ground color, intensity
scene.add(hemiLight);

// Create a Cube
const loader = new THREE.TextureLoader();
const geometry = new THREE.IcosahedronGeometry(1, 12);
const material = new THREE.MeshStandardMaterial({
  map: loader.load("https://res.cloudinary.com/dwfdyavop/image/upload/v1736183969/8k_earth_nightmap_wcy5es.jpg"),
  // map: loader.load("color: 0x00ff00"),
});
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);


// Camera Position
camera.position.z = 5;

// Animation Loop
function animate() {
  requestAnimationFrame(animate);

  cube.rotation.x += 0.001;
  cube.rotation.y += 0.002;

  controls.update(); // Update controls (necessary for smooth interaction)
  renderer.render(scene, camera);
}

animate();
