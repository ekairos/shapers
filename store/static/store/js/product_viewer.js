$(document).ready(function () {

  let modelViewer = $("#model-viewer");
  let active3d = Boolean(modelViewer.length);
  let imageView = $("#image-view");

  function switchImageSrc(image) {
    imageView.attr('src', $(image).attr('src'));
  }

  function switchViewerToImage(image) {
    active3d = false;
    switchImageSrc(image);
    modelViewer.fadeOut(200, 'linear',
      imageView.delay(200).fadeIn(200, 'linear'));
  }

  function switchViewerTo3d () {
    active3d = true;
    imageView.fadeOut(200, 'linear',
      modelViewer.delay(200).fadeIn(200, 'linear'));
  }

  $(".product-tbn").click(function () {

    if ($(this).hasClass('product-tbn-3d')) {

      !active3d ? switchViewerTo3d() : {};

    } else {

      active3d ? switchViewerToImage(this) : switchImageSrc(this);

    }
  });
});