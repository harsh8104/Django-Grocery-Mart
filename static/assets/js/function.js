$("#commentForm").submit(function (e) {
  e.preventDefault();
  $.ajax({
    data: $(this).serialize(),
    method: $(this).attr("method"),
    url: $(this).attr("action"),
    datatype: "json",
    success: function (response) {
      // console.log(response);

      if (response.bool) {
        $("#review-res").html("Review added successfully!!!");
        $(".hide-comment-form").hide();
        $(".add-review").hide();

        var d = new Date();
        const monthNames = [
          "Jan",
          "Feb",
          "Mar",
          "April",
          "May",
          "Jun",
          "July",
          "Aug",
          "Sept",
          "Oct",
          "Nov",
          "Dec",
        ];
        var strDate =
          d.getDate() + " " + monthNames[d.getMonth()] + "," + d.getFullYear();

        let _html =
          '<div class="single-comment justify-content-between d-flex mb-30">';
        _html += '<div class="user justify-content-between d-flex">';
        _html += '<div class="thumb text-center">';
        _html +=
          '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/2048px-Default_pfp.svg.png" alt="" />';
        _html +=
          '<a href="#" class="font-heading text-brand">' +
          response.context.user +
          "</a>";
        _html += "</div>";

        _html += ' <div class="desc">';
        _html += '<div class="d-flex justify-content-between mb-10">';
        _html += '<div class="d-flex align-items-center">';
        _html += '<span class="font-xs text-muted date"></span>';
        _html += "</div>";

        for (let i = 1; i <= response.context.rating; i++) {
          _html += '<i class="fas fa-star text-warning"> </i>';
        }

        _html += "</div>";
        _html += '<p class="mb-10">' + response.context.review + "</p>";

        _html += "</div>";
        _html += "</div>";
        _html += "</div>";
        $(".comment-list").prepend(_html);
        $(".date").html(strDate);
      }
    },
  });
});

$(document).ready(function () {
  $("#exampleCheckbox").on("click", function () {
    console.log("Check box clicked");
  });
});
