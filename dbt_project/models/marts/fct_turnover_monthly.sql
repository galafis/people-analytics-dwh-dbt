with headcount as (
    select * from {{ ref('fct_headcount_monthly') }}
),

turnover as (
    select
        report_month,
        department,
        report_year,
        report_month_num,
        report_quarter,
        active_headcount,
        terminations,
        voluntary_terminations,
        involuntary_terminations,
        new_hires,

        -- Teaching definition: terminations / ending headcount * 100.
        -- Zero ending headcount produces zero; do not interpret it as no departures.
        case
            when active_headcount > 0
            then round(terminations * 100.0 / active_headcount, 2)
            else 0
        end as turnover_rate,

        case
            when active_headcount > 0
            then round(voluntary_terminations * 100.0 / active_headcount, 2)
            else 0
        end as voluntary_turnover_rate,

        case
            when active_headcount > 0
            then round(involuntary_terminations * 100.0 / active_headcount, 2)
            else 0
        end as involuntary_turnover_rate,

        -- net change
        new_hires - terminations as net_headcount_change

    from headcount
)

select * from turnover
