<template>
  <div class="overlay">
    <svg class="loader" viewBox="0 0 24 24">
      <circle class="loader__value" cx="12" cy="12" r="10" />
      <circle class="loader__value" cx="12" cy="12" r="10" />
      <circle class="loader__value" cx="12" cy="12" r="10" />
      <circle class="loader__value" cx="12" cy="12" r="10" />
      <circle class="loader__value" cx="12" cy="12" r="10" />
      <circle class="loader__value" cx="12" cy="12" r="10" />
    </svg>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="scss" scoped>
// =============================
// Global
// =============================

html,
body {
  height: 100%;
}

body {
  align-items: center;
  display: flex;
  justify-content: center;
}

// =============================
// Loader
// =============================

$loader-colors: dodgerblue, mediumspringgreen, crimson, peachpuff, chocolate, pink;
$loader-dash: 63;
$loader-duration: length($loader-colors) * 1s;
$loader-duration-alt: $loader-duration / length($loader-colors);
$loader-keyframe: 1 / (length($loader-colors) * 2) * 100;

.loader {
  animation: loader-turn $loader-duration-alt linear infinite;
  padding: 1rem;
  max-width: 60px;
  width: 100%;

  @keyframes loader-turn {
    50% { transform: rotate(180deg) }
    100% { transform: rotate(720deg) }
  }
}

.loader__value {
  animation: loader-stroke $loader-duration linear infinite;
  fill: none;
  stroke-dasharray: $loader-dash;
  stroke-dashoffset: $loader-dash;
  stroke-linecap: round;
  stroke-width: 4;

  @for $i from 1 through length($loader-colors) {
    &:nth-child(#{$i}) {
      stroke: nth($loader-colors, $i);

      @if $i > 1 {
        animation-delay: ($i - 1) * $loader-duration-alt;
      }
    }
  }

  @keyframes loader-stroke {
    #{$loader-keyframe * 1%} { stroke-dashoffset: 0 }
    #{$loader-keyframe * 2%}, 100% { stroke-dashoffset: $loader-dash }
  }
}

.overlay {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 30;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
}

</style>
