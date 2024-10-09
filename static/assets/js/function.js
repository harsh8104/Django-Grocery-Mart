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
  $(".filter-checkbox").on("click", function () {
    console.log("Check box clicked");

    let filter_object = {};
    $(".filter-checkbox").each(function () {
      let filter_value = $(this).val();

      let filter_key = $(this).data("filter");

      filter_object[filter_key] = Array.from(
        document.querySelectorAll(
          "input[data-filter=" + filter_key + "]:checked"
        )
      ).map(function (element) {
        return element.value;
      });

      console.log(filter_object);

      $.ajax({
        url: "/filter-products",
        data: filter_object,
        dataType: "json",
        beforeSend: function () {
          console.log("Loading Data");
        },
        success: function (res) {
          console.log(res.data);

          $("#filtered-product").html(res.data);
        },
      });
    });
  });
  $("#max_price").on("blur",function(){
    let min_price=$(this).attr("min")
    let max_price=$(this).attr("max")
    let curr_price=$(this).val()
    
    if((curr_price < parseInt(min_price)) || (curr_price > parseInt(max_price)))
    {
      min_Price=Math.round(min_price*100)/100
      max_Price=Math.round(max_price*100)/100

      alert("Price must be between"+" "+min_Price+" "+"and"+" "+max_Price)
      
      $(this).val(min_Price)
      $("#range").val(min_price)
      $(this).focus()
      
      return false
    }

  })
});


