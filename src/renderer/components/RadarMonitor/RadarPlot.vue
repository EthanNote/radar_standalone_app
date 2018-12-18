<template>
  <div>
    <h3>雷达</h3>
    <div id="plot">
      <!-- <svg id="svg" viewBox="0,0,500,500" width="100%" height="100%">
            <g :transform="transform_str">
                <line v-for="l in lines" :x1="l[0]" :y1="l[1]" :x2="l[2]" :y2="l[3]" />
            </g>
            <g :transform="transform_str">
                <polyline v-for="l in polylines" :points="l"></polyline>
            </g>
      </svg>-->
      <canvas id="canvas" width="800" height="600"></canvas>
    </div>
  </div>
</template>
<script id="vertex-shader" type="x-shader/x-vertex">
import { connect } from "net";
import { log } from "util";

    attribute vec2 position;
    varying vec2 uv;
    void main() {
       gl_Position = vec4(position, 0, 1);
       uv = position;
    }
</script>

<script>
window.plotshow = function () {
  console.log('SHOW')
}
export default {
  data () {
    return {}
  },

  computed: {},

  methods: {},

  mounted () {
    var vert = `
    attribute vec3 position;
    varying float heat;
    void main() {
       gl_Position = vec4(position.xy,0.0, 1.0);
       heat = float(position.z);
    }    
    `
    var frag = `
    precision mediump float;
    varying float heat;
    void main() {
      gl_FragColor = vec4(vec3(heat, 0.4-heat, 1.0 - heat), heat+0.4);
    }
    `

    var canvas = document.getElementById('canvas')
    console.log('CANVAS', canvas)
    var gl = canvas.getContext('experimental-webgl')
    console.log('GL', self.gl)

    var vertShader = gl.createShader(gl.VERTEX_SHADER)
    var fragShader = gl.createShader(gl.FRAGMENT_SHADER)
    // var geomShader = gl.createShader(gl.GEOMETRY_SHADER)
    gl.shaderSource(vertShader, vert)
    gl.shaderSource(fragShader, frag)
    // gl.shaderSource(geomShader, geom)
    gl.compileShader(vertShader)
    gl.compileShader(fragShader)
    // gl.compileShader(geomShader)

    var program = gl.createProgram()
    gl.attachShader(program, vertShader)
    gl.attachShader(program, fragShader)
    // gl.attachShader(program, geomShader)
    gl.linkProgram(program)
    gl.useProgram(program)

    var buffer = gl.createBuffer()
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer)

    var points = [
      [-0.6, 0.6, 0.0],
      [-0.54, 0.6426, 0.05],
      [-0.48, 0.6528, 0.1],
      [-0.42, 0.6342, 0.15],
      [-0.36, 0.5904, 0.2],
      [-0.3, 0.525, 0.25],
      [-0.24, 0.4416, 0.3],
      [-0.18, 0.3438, 0.35],
      [-0.12, 0.2352, 0.4],
      [-0.06, 0.1194, 0.45],
      [-0.0, 0.0, 0.5],
      [0.06, -0.1194, 0.55],
      [0.12, -0.2352, 0.6],
      [0.18, -0.3438, 0.65],
      [0.24, -0.4416, 0.7],
      [0.3, -0.525, 0.75],
      [0.36, -0.5904, 0.8],
      [0.42, -0.6342, 0.85],
      [0.48, -0.6528, 0.9],
      [0.54, -0.6426, 0.95],
      [0.6, -0.6, 1.0]]
    // var points = [[-0.5, -0.5, 1.0], [-0.2, 0.0, 1], [0.0, 0.0, 1.0]]
    var pointsVertexGen = function (points) {
      var result = []
      var rad = 0.02
      for (var i in points) {
        result = result.concat([points[i][0] - rad, points[i][1] - rad, points[i][2]])
        result = result.concat([points[i][0] + rad, points[i][1] - rad, points[i][2]])
        result = result.concat([points[i][0] - rad, points[i][1] + rad, points[i][2]])

        result = result.concat([points[i][0] - rad, points[i][1] + rad, points[i][2]])
        result = result.concat([points[i][0] + rad, points[i][1] - rad, points[i][2]])
        result = result.concat([points[i][0] + rad, points[i][1] + rad, points[i][2]])
      }
      console.log(result)
      console.log(result)
      return result
    }

    gl.bufferData(
      gl.ARRAY_BUFFER,
      // new Float32Array([-1, -1, 0, 1, -1, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
      new Float32Array(pointsVertexGen(points)),
      gl.STATIC_DRAW
    )
    var positionLocation = gl.getAttribLocation(program, 'position')

    gl.enableVertexAttribArray(positionLocation)
    gl.vertexAttribPointer(positionLocation, 3, gl.FLOAT, false, 0, 0)
    // draw
    gl.drawArrays(gl.TRIANGLES, 0, 126)
  }
}
</script>

<style>
#canvas {
  width: 100%;
}
</style>


