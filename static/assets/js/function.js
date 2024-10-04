$("#commentForm").submit(function (e) {
  e.preventDefault();

  $.ajax({
    data: $(this).serialize(),
    method: $(this).attr("method"),
    url: $(this).attr("action"),
    datatype: "json",
    success: function (response) {
      console.log(response);

      if (response.bool) {
        $("#review-res").html("Review added successfully!!!");
      }
    },
  });
});
